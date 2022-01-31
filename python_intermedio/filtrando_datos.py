DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def print_list(selected_list, element_to_list, string):
    maxlength = max(list(map(lambda x: len(x[element_to_list]), selected_list)))
    print(" ", string)
    print("╒═", maxlength*"═", end="═╕\n", sep="")
    for worker in selected_list:
        print("│ ", worker[element_to_list], (maxlength+1-len(worker[element_to_list]))*" ", "│",sep="")
    print("╘═", maxlength*"═", end="═╛\n\n", sep="")
    pass

def run():

    # Usando filter
    all_python_devs = list(filter(lambda worker: worker["language"] == "python" , DATA))
    # Usando filter y map
    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    # all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))
    # Usando list compehensions
    # old_people = [worker["name"] for worker in DATA if worker["age"]>=70]
    old_people = [worker for worker in DATA if worker["age"]>=70]
    # adults = [worker["name"] for worker in DATA if worker["age"]>=18]
    adults = [worker for worker in DATA if worker["age"]>=18]
    
    print_list(all_python_devs, "name","Python")
    print_list(all_platzi_workers, "name","Platzi")
    print_list(old_people, "name","Old people")
    print_list(adults, "name", "Old people")

if __name__ == '__main__':
    run()