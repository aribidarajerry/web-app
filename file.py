
# Your simple text file editor app


def convert_str_to_dict(obj):
    import ast
    new_obj = ast.literal_eval(obj)
    return new_obj


# --------------------------------------------------------------------------------------------------------------


# This function creates a new file, reads and displays the content(s) of a file
def get(file_name):
    # An empty variable to store file content
    content = ''

    # This code is to prevent FileNotFoundError from the next block of code and 'a' to prevent emptying file when writing
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write('')

    # Read file and concatenate it's content to the empty variable
    with open(file_name, encoding='utf-8') as f:
        content += f.read()

    # Return the content of the file
    return content


# --------------------------------------------------------------------------------------------------------------


# This function checks if a particular data or text is already in the file whose contents have been converted into a list
def exist(text, lst):

    # Loop over each data to check if any one already exist
    for l in lst:
        if text==l:
            # Return the index of the the text in the list
            return lst.index(text)


# --------------------------------------------------------------------------------------------------------------


# This block writes data into a file only if the data doesn't exist in the file already
def write(file_name, data):

    # Get the content of the file using the 'get' function
    content = get(file_name)

    # Split each data from a newline (\n) into a list for easy search
    content_lst = content.split('\n')
    print(f'File content: {content_lst}')

    # Open the file for writing
    with open(file_name, 'w', encoding='utf-8') as f:

        # Check if the text exist already to avoid duplication
        if exist(data, content_lst) != None:
            print('Already exist!')
            f.write(content)
        elif data:
            # If the content is already empty, just make it the text no need for concatenating to prevent loop holes
            if content == '':
                content = data
            else:
                # When I want to write on a new file to show organisation, each data much appear on a new line
                content += '\n' + data
            f.write(content)
            print(f'Content written to {file_name}!')
        else:
            print('Invalid input!')
            f.write(content)


# --------------------------------------------------------------------------------------------------------------


def delete(file_name):

    # Get the content of the file using the 'get' function
    content = get(file_name)

    # Split each data from a newline (\n) into a list for easy search
    content_lst = content.split('\n')
    print(content_lst)
    with open(file_name, 'w', encoding='utf-8') as f:
        text=input('Enter text: ')

        # Check if text exist
        if exist(text, content_lst) != None:
            index = exist(text, content_lst)
            
            # delete text through it's index from exist()
            del content_lst[index]

            # Convert the remaining data in the list to strings then write to file
            content = '\n'.join(content_lst)
            f.write(content)
            print(f"Content deleted from {file_name}!")
        else:
            print('Does not exist')
            f.write(content)


# --------------------------------------------------------------------------------------------------------------


def clear_file(file_name):
    # Get file to prevent FileNotFoundError when writing to file
    get(file_name)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write('')
        return f"{file_name} has been successfully cleared!"


# --------------------------------------------------------------------------------------------------------------




# file = 'password_manager.txt'
# instruction = input('What do you want to do? (Read(r), write(w), delete(d)): ')
# if instruction == 'r':
#     print(get(file))
# elif instruction == 'w':
#     write(file)
# else:
#     delete(file)


obj = {
    'name': 'jerry',
    'age': 20
}


