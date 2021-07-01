import requests
import json
import datetime

# API Key: 32d01950-8108-47db-ae16-797b8e6f4171
def check_method(user_email):
    verified = False
    print("User Email: {}".format(user_email))
    url = 'https://securityiq.infosecinstitute.com/api/v1/learners'
    headers = {"Authorization": "Bearer 32d01950-8108-47db-ae16-797b8e6f4171"}
    response = requests.get(url, headers=headers)

    #pass learner by email
    url = 'https://securityiq.infosecinstitute.com/api/v1/learners/?email={}'.format(user_email)
    learner_response = requests.get(url,headers=headers)
    #extract learner ID
    learner = (learner_response.json())
    learner_data = learner['data']
    #fetches ID from nested JSON dict
    id = ''
    for item in learner_data:
        id = item['id']
        print("Learner ID: {}".format(id))

    url = 'https://securityiq.infosecinstitute.com/api/v1/learners/{}'.format(id)
    learner_fetch = requests.get(url, headers=headers)
    learner_individual = (learner_fetch.json())
    learner_stat= (learner_individual['learner_stat'])
    module_completed_count = learner_stat['module_completed_count']
    if module_completed_count >= 6:
        verified = True
        print("User has completed enough training.")
    else:
        print("User has NOT completed required training.")
    print("Completed Count: {}".format(module_completed_count))

if __name__ == "__main__":
    email = input("user email: ")
    try:
        check_method(email)
    except Exception as e:
        print("ERROR: " + str(e))



