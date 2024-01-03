#dictinarin in 


travel_log =[
    {
        "country":"france",
        "vistis":23,
        "citys": ["prish","lilly","dijon"]
    },
    {
        "country":"germany",
        "vistis":2,
        "citys": ["berlin","hamburg","stuttgart"]
    },
]



def add_new_contry(country_name,times_visit,citys_visited):
    new_contry={}
    new_contry["country"] = country_name
    new_contry["vistis"] = times_visit
    new_contry["citys"] = citys_visited
    travel_log.append(new_contry)

add_new_contry("india",3,["surat",'alkf','dsaf'])


print(travel_log)