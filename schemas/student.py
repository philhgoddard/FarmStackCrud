#schemas help to serialize and also convert mongodb format jsaon to
#our UI needed json
# meaning the db may bring back much more data for the item
# but this schema allows you to control how much you want to give back to the UI


# get the json format from the raw database format
def studentEntity(db_item) -> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone": db_item["student_phone"]
    }

# this is called from route (/students) to get a list of students from database
def listOfStudentEntity(db_item_list) -> list:
    list_student_entity = []
    for item in db_item_list:   # iterate over database record
        list_student_entity.append(studentEntity(item))  #convert each item to json

    return list_student_entity

#update a student
