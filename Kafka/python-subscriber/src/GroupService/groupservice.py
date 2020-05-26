import os
import yaml

def get_groups():

    # get location
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    # load yaml file
    yamlgroup = yaml.load_all(open(os.path.join(__location__, 'groups.yaml')), Loader=yaml.FullLoader)

    # save to dict
    groups = {}
    for data in yamlgroup:
        groups[data["groupid"]] = data["groupmembers"]
    
    keys = list(groups.keys())
    
    return groups, keys

def get_group_members(reciever_id, sender_id):

    # load groups and keys
    groups, keys = get_groups()
    
    # remove sender from group
    recievers = groups[reciever_id]
    recievers.remove(sender_id)

    # return all recievers of message
    return recievers