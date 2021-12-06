# Below personalized group details - details should be personalized and used within the project

group_name_short = "OSP"
group_name_full = "Ochotnicza Straż Pożarna"
specialisation_short = "SAR"
specialisation_full = "Search and Rescue"

permitted_superuser = ("Natalia Czapska",)
permitted_admin = ("Natalia Czapska", "Katarzyna W.",)


def get_group_name_short():
    return group_name_short


def get_group_name_full():
    return group_name_full


def get_specialisation_short():
    return specialisation_short


def get_specialisation_full():
    return specialisation_full
