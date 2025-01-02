import os

input_dir = './animation_frames/'
output_dir = './animation_frames_converted/'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Read the content of the .txt file
        with open(os.path.join(input_dir, filename), 'r') as file:
            content = file.read()

        # Replace line breaks with \n
        content = content.replace('\n', '\\n')

        # Replace HTML tags with ANSI escape codes
        content = content.replace('<span class="b">', '\\033[1;34m')
        content = content.replace('</span>', '\\033[0;0m')

        # Create the corresponding .c file
        c_filename = filename.replace('.txt', '.c')
        variable_name = filename.replace('.txt', '')
        with open(os.path.join(output_dir, c_filename), 'w') as file:
            file.write(f'const char* {variable_name} = "{content}";\n')

output_file = 'all_frames.c'

with open(output_file, 'w') as f:
    for filename in os.listdir(output_dir):
        if filename.endswith('.c'):
            f.write(f'#include "{output_dir}{filename}"\n')
    
    f.write(f'\nconst char* frames[{len(os.listdir(output_dir))}];\n\n')
    
    f.write(f'const int num_frames = {len(os.listdir(output_dir))};\n\n')
    
    f.write('void init_frames() {\n')
    
    for filename in os.listdir(output_dir):
        if filename.endswith('.c'):
            variable_name = filename.replace('.c', '')
            frame_number = int(variable_name.replace('frame_', '')) - 1
            f.write(f'    frames[{frame_number}] = {variable_name};\n')
            
    f.write('}\n')