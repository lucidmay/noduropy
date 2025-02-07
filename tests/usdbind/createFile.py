from pxr import Usd, Sdf, Ar

def create_usda_with_maya_reference(output_path, maya_file_path):
    usda_content = f"""#usda 1.0

    def "MayaReference" (
        prepend references = @"{maya_file_path}"
    )
    {{
    }}
    """

    with open(output_path, "w") as usda_file:
        usda_file.write(usda_content)

    print(f"USDA file created at: {output_path}")

# Example usage
maya_file_path = "/path/to/your/maya_file.ma"  # Change this to your Maya file path
output_usda_path = "output.usda"  # Change this to your desired USDA output file path

create_usda_with_maya_reference(output_usda_path, maya_file_path)
