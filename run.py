import os
import time
import subprocess

        
def docker_menu():
    default_image_name = "bot-run-test-v1"
    default_container_name = "bot-run-test-v1-container"
    port = "80:45441"
    #ssssasdasd 111
    while True:
        print("\nDocker Management Menu V.0.0.1")
        print("0. Auto ReBuild")
        print("1. Build Docker Image")
        print("2. List Docker Images")
        print("3. Run Docker Container")
        print("4. Show Docker Logs")
        print("5. List Docker Containers")
        print("6. Stop and Remove Docker Container")
        print("7. Remove Docker Image")
        print("8. Edit requirements.txt")
        print("9. Exit")
        print("10. View Server Use")
        print("11. Install_Docker")
        print("12. Install_Python")
        print("13. Install_MongoDB")
        print("14. Install_SSH")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            # Build Docker image
            os.system(f"docker build -t {default_image_name} .")
            os.system("docker images")
        elif choice == "2":
            # List Docker images
            os.system("docker images")
        
        elif choice == "3":
            # Run Docker container
            port = "80:45441"
            os.system(f"docker run -d --restart always -p {port} --name {default_container_name} {default_image_name}")
            os.system("docker ps -a")
        elif choice == "4":
            # Show logs of a container
            container_ID = subprocess.check_output(
                    f"docker ps --filter 'name={default_container_name}' -q", shell=True, text=True
                ).strip()
            
            os.system(f"docker logs {container_ID}")
        
        elif choice == "5":
            # List Docker containers
            os.system("docker ps -a")
        
        elif choice == "6":
            # Stop and remove a container
            container_name = input("Enter the container name or ID to stop and remove: ").strip()
            if not container_name:
                print("Container name or ID is required!")
                continue
            
            os.system(f"docker stop {container_name}")
            os.system(f"docker rm {container_name}")
        
        elif choice == "7":
            # Remove Docker image
            
            os.system(f"docker rmi {default_image_name}")
        
        elif choice == "8":
            os.system(f"nano requirements.txt")
            
        elif choice == "0":
            print(f"docker ps --filter 'name={default_container_name}' -q")
            container_ID = subprocess.check_output(
                    f"docker ps --filter 'name={default_container_name}' -q", shell=True, text=True
                ).strip()
            print(f"docker stop {container_ID}")
            os.system(f"docker stop {container_ID}")
            print(f"docker rm {container_ID}")
            os.system(f"docker rm {container_ID}")
            print(f"docker rmi {default_image_name}")
            os.system(f"docker rmi {default_image_name}")
            
            print(f"docker build -t {default_image_name} .")
            os.system(f"docker build -t {default_image_name} .")
            
            print(f"docker run -d --restart always -p {port} --name {default_container_name} {default_image_name}")
            os.system(f"docker run -d --restart always -p {port} --name {default_container_name} {default_image_name}")
            time.sleep(2)
            print("wait Log.....3")
            time.sleep(2)
            print("wait Log.....2")
            time.sleep(2)
            print("wait Log.....1")
            container_ID = subprocess.check_output(
                    f"docker ps --filter 'name={default_container_name}' -q", shell=True, text=True
                ).strip()
            print(f"docker logs {container_ID}")
            os.system(f"docker logs {container_ID}")
            
        elif choice == "9":
            # Exit
            print("Exiting Docker Management.")
            break
        elif choice == "10":
            os.system("df -h")
            os.system("top")
        elif choice == "11":
            Install_Docker()
        elif choice == "12":
            Install_Python()
        elif choice == "13":
            Install_MongoDB()
        elif choice == "14":
            Install_SSH()
        else:
            print("Invalid choice. Please try again.")

# 1 -CopyFile ToServer
# 2 -Remote SSH Server
# 3 -Run Install_Docker
# 4 -Run Install_MongoDB
# 5 -Run Deploy Auto 
def Install_SSH():
    os.system("sudo apt update")
    os.system("sudo apt install openssh-server")
    os.system("sudo systemctl start ssh")
    os.system("sudo systemctl enable ssh")
    os.system("sudo systemctl status ssh")
def Install_Docker():
    os.system("sudo apt update")
    os.system("sudo apt install apt-transport-https ca-certificates curl software-properties-common -y")
    os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -")
    os.system("sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'")
    os.system("sudo apt update")
    
    os.system("sudo apt install docker-ce -y")
    os.system("docker --version")
    
def Install_Python():
    os.system("sudo apt update")
    os.system("sudo apt install python3 python3-pip -y")
   
    
def Install_MongoDB():
    os.system("sudo apt update")
    os.system("wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -")
    os.system("echo 'deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse' | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list")
    os.system("sudo apt update")
    os.system("sudo apt install mongodb-org")
    os.system("sudo systemctl start mongod")
    os.system("sudo systemctl enable mongod")
    os.system("sudo apt update")
    os.system("sudo apt install net-tools -y")
  

    

if __name__ == "__main__":
    docker_menu()

# pyinstaller --onefile run.py