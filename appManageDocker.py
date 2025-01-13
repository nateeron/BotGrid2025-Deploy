import os

def docker_menu():
    default_image_name = "bot-run-test-v1"
    while True:
        print("\nDocker Management Menu")
        print("1. Build Docker Image")
        print("2. List Docker Images")
        print("3. Run Docker Container")
        print("4. Show Docker Logs")
        print("5. List Docker Containers")
        print("6. Stop and Remove Docker Container")
        print("7. Remove Docker Image")
        print("8. Edit requirements.txt")
        print("9. Exit")
        
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
            default_container_name = "bot-run-test-v1-container"
            port = "80:45441"
            os.system(f"docker run -d --restart always -p {port} --name {default_container_name} {default_image_name}")
            os.system("docker ps -a")
        elif choice == "4":
            # Show logs of a container
            container_name = input("Enter the container name or ID: ").strip()
            if not container_name:
                print("Container name or ID is required!")
                continue
            
            os.system(f"docker logs {container_name}")
        
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
        elif choice == "9":
            # Exit
            print("Exiting Docker Management.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    docker_menu()
