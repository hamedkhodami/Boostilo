from django.utils import timezone
from os.path import splitext


# Get time in format
def get_time(frmt: str = '%Y-%m-%d %H:%M'):
    now = timezone.now()
    if frmt is not None:
        now = now.strftime(frmt)

    return now

# Create image/file path based on time
def upload_file_src(instance, path):
    now = get_time('%Y-%m-%d')
    return f'files/{now}/{path}'

# Return file extension
def get_file_extension(file_name):
    name, extension = splitext(file_name.file.name)
    return extension