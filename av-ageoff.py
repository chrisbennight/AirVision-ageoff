import httplib2
import urllib
import time
import json

#settings to change
airvisionURLBase = 'https://localhost:7443/'

airvisionUser = 'your.airvision@login.com'
airvisionPass = 'yourAirvisionPassword'
durationToKeep = 14  #number of days back to keep (14 = 2 weeks)

#don't change
airvisionAPI = airvisionURLBase + 'api/2.0/'

#get login cookie
loginPayload = {'email' : airvisionUser, 'password' : airvisionPass, 'login' : 'Login'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}
http = httplib2.Http(disable_ssl_certificate_validation=True)
response, content = http.request(airvisionURLBase + 'login', 'GET', headers=headers)
response, content = http.request(airvisionURLBase + 'login', 'POST', headers=headers, body = urllib.urlencode(loginPayload))
headers = response

#get all recording id's in range
startTime = 0
endTime = time.time() - durationToKeep * 24 * 60 * 60
response, content = http.request(airvisionAPI + 'recording?start=%d&end=%d' % (startTime, endTime), 'GET', headers=headers)
recordings = json.loads(content)
recordingids = 


#delete recordings
deletePayload = {'ids' : recordingids}
response, content = http.request(airvisionAPI + 'recording', 'DELETE', headers=headers, body = json.dumps(deletePayload))
