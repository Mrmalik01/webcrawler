import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    print("Directory created")

def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
        f.close()

def create_data_files(code_directory, base_url):

    # Complete file path for both files
    queue = os.path.join(code_directory, "queue.txt")
    crawled = os.path.join(code_directory, "crawled.txt")

    # Create files
    if not os.path.isfile(queue):
        write_file(queue, base_url)
        print("Queue file created")
    if not os.path.isfile(crawled):
        write_file(queue, base_url)
        print("Crawled file created")


def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data, '\n')
        f.close()

def delete_file_contents(path):
    open(path, 'w').close()


def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace("\n", ""))
        f.close()
        print("Read links from the file")
    return results

def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l+"\n")
        f.close()
        print("Written links to the file")


