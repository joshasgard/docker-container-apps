n = int (input ("Please enter any positive whole number: "))

if n < 0:
    print("Error: Number must be positive")
else:
    sum = 0
    i = n
    while i > 0:
        sum += i
        i -= 1
    print ("Sum of all positive numbers from 1 till",n,"is",sum)

# docker run -it -v ${PWD}:/app python:alpine python /app/main.py
# ====Docker code above pulls alpine python image from docker hub, runs a container off it, 
# connects the container to local pc file, runs the specified python app/command 
# and exits=====