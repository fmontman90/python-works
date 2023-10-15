#Example of try and if run twice error should produce.


file_name = 'recipes.txt'
#start of try block to catch error
try:
    my_file = open('recipes.txt','x')
    my_file.write('Meatballs\n')
    my_file.close()
except FileExistsError as err:
    print(f'The {file_name} file already exists.')
except:
    print(f'Unable to write to file')
else:
    print(f'Wrote to {file_name}')
finally:
    print("Execution completed")


    