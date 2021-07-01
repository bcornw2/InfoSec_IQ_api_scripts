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
    groups = learner_individual['groups']
    groups_data = groups['data']

    #list groups
    print("Groups: \n ___________ \n")
    group_array = []
    for group in groups_data:
        group_array.append(group['name'])
    print(group_array)
    if "Field Staff" in group_array:
        campaign_name = "Field Staff - Annual Training"
    if "General Staff" in group_array:

        campaign_name = ''
        date = datetime.date.today()

        quarter = ((date.month - 1)//3) + 1
        if quarter == 4: #first quarter when call occurs, previous quarter must be checked
            campaign_name = "Q3 - Quarterly Campaign"
        if quarter == 1: #and so on
            campaign_name = "Q4 - Quarterly Campaign"
        if quarter == 2:
            campaign_name = "Q1 - Quarterly Campaign"
        if quarter == 3:
            campaign_name = "Q2 - Quarterly Campaign"

    url = 'https://securityiq.infosecinstitute.com/api/v1/campaigns/?name={}'.format(campaign_name)
    campaigns = requests.get(url, headers = headers)
    campaigns = campaigns.json()
    campaigns_data = campaigns['data']
    campaigns_id = ''
    for set in campaigns_data:
        campaigns_id = set['id']
    print("Campaign ID: " + campaigns_id)

    #find info on campaigns
    url = "https://securityiq.infosecinstitute.com/api/v1/campaigns/{}/runs/".format(campaigns_id)
    runs = requests.get(url, headers = headers)
    runs = runs.json()
    runs_data = runs['data']
    earliest = datetime.date.min
    run_id = ''
    date_dict = {}
    for run in runs_data:
        run_id = run['id']
        start_date = run['start']
        start_date = start_date[:-15] #strips time from date
        datetime_object = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        print("Start Date: " + start_date + ", " + str(datetime_object))
        date_dict[datetime_object] = run_id
        print(str(date_dict))
        #use only most recent campaign run
        if datetime_object > earliest:
            earliest = datetime_object

    run_id = date_dict.get(earliest)
    print("RUN ID: " + str(run_id))

   # print("DATE_DICT " + str(date_dict))
   # if len(date_dict) <= 1:
   #     print("    only one key, only one run")
   #     run_id = run_id
   #     print("date_dict.keys[1]= : " + str(run_id))
   # else:
   #     pass

    url = 'https://securityiq.infosecinstitute.com/api/v1/campaigns/{}/runs/{}/learners/?email={}'.format(campaigns_id, run_id, user_email)
    print(url)
    completed = requests.get(url, headers=headers)
    print(completed.json())


    module_completed_count = learner_stat['module_completed_count']
    if module_completed_count >= 6:
        verified = True
        print("User has completed enough training.")
    else:
        print("User has NOT completed required training.")
    print("Completed Count: {}".format(module_completed_count))

if __name__ == "__main__":
    email = input("user email: ")
 #   try:
    check_method(email)
  #  except Exception as e:
    #print("ERROR: " + str(e))



