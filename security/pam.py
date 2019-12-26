# PAM interface in python, launches compare.py

# Import required modules
import subprocess
import sys
import os
import glob
# pam-python is running python 2, so we use the old module here
import ConfigParser

# Read config from disk
import requests

config = ConfigParser.ConfigParser()
config.read(os.path.dirname(os.path.abspath(__file__)) + "/config.ini")


def doAuth(pamh):
	"""Starts authentication in a seperate process"""

	# Abort is Howdy is disabled
	if config.getboolean("core", "disabled"):
		sys.exit(0)

	# Abort if we're in a remote SSH env
	if config.getboolean("core", "ignore_ssh"):
		if "SSH_CONNECTION" in os.environ or "SSH_CLIENT" in os.environ or "SSHD_OPTS" in os.environ:
			sys.exit(0)

	# Abort if lid is closed
	if config.getboolean("core", "ignore_closed_lid"):
		if any("closed" in open(f).read() for f in glob.glob("/proc/acpi/button/lid/*/state")):
			sys.exit(0)

	# Alert the user that we are doing face detection
	if config.getboolean("core", "detection_notice"):
		pamh.conversation(pamh.Message(pamh.PAM_TEXT_INFO, "Attempting face detection"))

	# Run compare as python3 subprocess to circumvent python version and import issues
	status = subprocess.call(["/usr/bin/python3", os.path.dirname(os.path.abspath(__file__)) + "/compare.py", pamh.get_user()])

	# Status 10 means we couldn't find any face models
	if status == 10:
		if not config.getboolean("core", "suppress_unknown"):
			pamh.conversation(pamh.Message(pamh.PAM_ERROR_MSG, "No face model known"))
		return pamh.PAM_USER_UNKNOWN
	# Status 11 means we exceded the maximum retry count
	elif status == 11:
		pamh.conversation(pamh.Message(pamh.PAM_ERROR_MSG, "Face detection timeout reached"))
		return pamh.PAM_AUTH_ERR
	# Status 12 means we aborted
	elif status == 12:
		return pamh.PAM_AUTH_ERR

	elif status == 13:
		pamh.conversation(pamh.Message(pamh.PAM_ERROR_MSG, "You are unidentified"))
		return pamh.PAM_AUTH_ERR

	elif status == 14:
		pamh.conversation(pamh.Message(pamh.PAM_ERROR_MSG, "Multiple face detected. Please try again."))
		return pamh.PAM_AUTH_ERR

	elif status == 15:
		pamh.conversation(pamh.Message(pamh.PAM_ERROR_MSG, "No face detected. Please try again."))
		return pamh.PAM_AUTH_ERR

	elif status == 16:
		pamh.conversation(pamh.Message(pamh.PAM_ERROR_MSG, "No camera found. Please connect to a camera device."))
		return pamh.PAM_AUTH_ERR

	# Status 0 is a successful exit
	elif status == 0:
		# Show the success message if it isn't suppressed


		if not config.getboolean("core", "no_confirmation"):
			#pamh.conversation(pamh.Message(pamh.PAM_TEXT_INFO, "Identified face as " + pamh.get_user()))
			r = open('/lib/security/howdy/username.txt', "r")
			contents = r.read()

			position = contents.find('-', 0)
			length = len(contents)
			position_matric = contents.find(':', 0)

			uid = contents[0:position]
			name = contents[position + 1:position_matric]
			matric = contents[position_matric + 1:length]
			fullname = name.replace("_", " ")

			# matric_data = {'student_id':matric
			#         }
			#
			# sendmatric = requests.post(url='https://pure-headland-78653.herokuapp.com/api/resources/emotion', data=matric_data)
			# print(sendmatric)
			#
			# uid_data = {'id': uid
			# 			   }
			#
			# sendmatric = requests.post(url='https://pure-headland-78653.herokuapp.com/api/resources/emotion', data=matric_data)
			# print(sendmatric)

			pamh.conversation(pamh.Message(pamh.PAM_TEXT_INFO, "Authenticated user: " + fullname + "-" + matric))


		return pamh.PAM_SUCCESS

	# Otherwise, we can't discribe what happend but it wasn't successful
	pamh.conversation(pamh.Message(pamh.PAM_ERROR_MSG, "Unknown error: " + str(status)))
	return pamh.PAM_SYSTEM_ERR


def pam_sm_authenticate(pamh, flags, args):
	"""Called by PAM when the user wants to authenticate, in sudo for example"""
	# return doAuth(pamh)
	# Abort is Howdy is disabled
	return doAuth(pamh)


def pam_sm_open_session(pamh, flags, args):
	"""Called when starting a session, such as su"""
	return doAuth(pamh)


def pam_sm_close_session(pamh, flags, argv):
	"""We don't need to clean anyting up at the end of a session, so returns true"""
	return pamh.PAM_SUCCESS


def pam_sm_setcred(pamh, flags, argv):
	"""We don't need set any credentials, so returns true"""
	return pamh.PAM_SUCCESS
