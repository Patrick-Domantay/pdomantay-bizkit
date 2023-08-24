from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    # THIS IS MY REVISED SEARCH CODE

    temp = []   
    
    for argkey, argvalue in args.items():
        for dict in USERS:
            for key, value in dict.items():
                if type(value) is int and argvalue.isdigit():
                        argvalue = int(argvalue)
                        lowerlimit = argvalue - 1
                        upperlimit = argvalue + 2 
                        arg_age = argvalue - 1
                        while lowerlimit < upperlimit: 
                            arg_age = str(arg_age)
                            value = str(value)
                            if argkey.lower() in key.lower() and arg_age.lower() in value.lower():
                                if dict not in temp:
                                    temp.append(dict)
                                    lowerlimit += 1
                                    arg_age = int(arg_age)
                                    arg_age += 1
                            arg_age = int(arg_age)
                            lowerlimit += 1
                            arg_age += 1
                else:
                    argvalue = str(argvalue)
                    value = str(value)
                    if argkey.lower() in key.lower() and argvalue.lower() in value.lower():
                        if dict not in temp:
                            temp.append(dict)

    if temp != []:
        return temp
    else:
        return USERS
    
    # END OF MY CODE





    # USERSLIST = []

    # priority_userdict = {}
    # desired_search_priority = ["id","name","age","occupation"]
    # for ogdict in USERS: 
    #     for desiredkey in desired_search_priority:     
    #         for ogkey, ogvalue in ogdict.items():
    #             if ogkey == desiredkey:
    #                 USERSLIST.append({ogkey:ogvalue})
    #                 priority_userdict[ogkey] = ogvalue
    #     d = {k:v for x in USERSLIST for k,v in x.items()}
    #     return USERSLIST