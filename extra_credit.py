import matplotlib.pyplot as plt

def duration(actor_name, avg_duration):
    plt.figure(figsize=(8, 6))
    plt.bar(actor_name, avg_duration, color='skyblue')
    plt.xlabel('Actor')
    plt.ylabel('Average Movie Duration (minutes)')
    plt.title('Average Movie Duration for Actor')
    plt.xticks(rotation=45)
    plt.show()

actor_name = "Jennifer Lopez"
avg_duration = 130  
duration(actor_name, avg_duration)
