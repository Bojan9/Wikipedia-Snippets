def replace_placeholders(template, values):
    for key, value in values.items():
        placeholder = f"<<{key}>>"
        template = template.replace(placeholder, str(value))
    return template

def main():
    # Read template file
    with open('01_slovenian-towns/template.txt', 'r', encoding='utf-8') as template_file:
        template_content = template_file.read()

    # Read values file
    with open('01_slovenian-towns/values.txt', 'r', encoding='utf-8') as values_file:
        values_content = values_file.read()

    # Parse values from the values file
    all_values = {}
    for line in values_content.split('\n'):
        if '=' in line:
            key, value_str = line.split('=', 1)
            values = [v.strip() for v in value_str.split(',')]
            all_values[key.strip()] = values

    # Generate output files for each set of values
    for i, set_values in enumerate(zip(*all_values.values())):
        current_values = {key: value[i] for key, value in all_values.items()}

        # Replace placeholders in the template with current values
        modified_content = replace_placeholders(template_content, current_values)

        # Write the modified content to a new file
        output_filename = f'output_{i + 1}.txt'
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(modified_content)

if __name__ == "__main__":
    main()
