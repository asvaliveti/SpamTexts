on run {phoneNumber, message}
    tell application "Messages"
    set targetService to id of 1st service whose service type = iMessage
    set theBuddy to buddy phoneNumber of service id targetService
    send message to theBuddy
    end tell
end run
