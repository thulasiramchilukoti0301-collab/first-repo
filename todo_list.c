#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TASK_LENGTH 200
#define MAX_TASKS 100
#define FILENAME "todo_list.txt"

// Structure to represent a task
typedef struct Task {
    int id;
    char description[MAX_TASK_LENGTH];
    int completed;
    struct Task* next;
} Task;

// Global variables
Task* head = NULL;
int taskIdCounter = 1;

// Function prototypes
void displayMenu();
void addTask();
void viewTasks();
void markComplete();
void deleteTask();
void saveToFile();
void loadFromFile();
void freeTasks();
void clearScreen();
void waitForEnter();
int getIntegerInput();

// Main function
int main() {
    int choice;
    
    // Load tasks from file if exists
    loadFromFile();
    
    printf("=====================================\n");
    printf("   WELCOME TO TODO LIST MANAGER\n");
    printf("=====================================\n\n");
    
    do {
        displayMenu();
        printf("Enter your choice: ");
        choice = getIntegerInput();
        
        switch(choice) {
            case 1:
                addTask();
                break;
            case 2:
                viewTasks();
                break;
            case 3:
                markComplete();
                break;
            case 4:
                deleteTask();
                break;
            case 5:
                saveToFile();
                printf("\nTasks saved successfully!\n");
                waitForEnter();
                break;
            case 6:
                loadFromFile();
                printf("\nTasks loaded successfully!\n");
                waitForEnter();
                break;
            case 0:
                printf("\nSaving tasks before exit...\n");
                saveToFile();
                printf("Thank you for using Todo List Manager!\n");
                freeTasks();
                break;
            default:
                printf("\nInvalid choice! Please try again.\n");
                waitForEnter();
        }
    } while(choice != 0);
    
    return 0;
}

// Display menu options
void displayMenu() {
    clearScreen();
    printf("=====================================\n");
    printf("           TODO LIST MENU\n");
    printf("=====================================\n");
    printf("1. Add Task\n");
    printf("2. View All Tasks\n");
    printf("3. Mark Task as Complete\n");
    printf("4. Delete Task\n");
    printf("5. Save Tasks to File\n");
    printf("6. Load Tasks from File\n");
    printf("0. Exit\n");
    printf("=====================================\n\n");
}

// Add a new task
void addTask() {
    Task* newTask = (Task*)malloc(sizeof(Task));
    Task* current;
    
    if(newTask == NULL) {
        printf("Memory allocation failed!\n");
        waitForEnter();
        return;
    }
    
    newTask->id = taskIdCounter++;
    newTask->completed = 0;
    newTask->next = NULL;
    
    printf("\nEnter task description: ");
    fflush(stdin);
    fgets(newTask->description, MAX_TASK_LENGTH, stdin);
    newTask->description[strcspn(newTask->description, "\n")] = 0; // Remove newline
    
    if(strlen(newTask->description) == 0) {
        printf("Task description cannot be empty!\n");
        free(newTask);
        waitForEnter();
        return;
    }
    
    if(head == NULL) {
        head = newTask;
    } else {
        current = head;
        while(current->next != NULL) {
            current = current->next;
        }
        current->next = newTask;
    }
    
    printf("\nTask added successfully! (ID: %d)\n", newTask->id);
    waitForEnter();
}

// View all tasks
void viewTasks() {
    Task* current = head;
    int taskCount = 0;
    int completedCount = 0;
    int pendingCount = 0;
    
    clearScreen();
    printf("=====================================\n");
    printf("          ALL TASKS\n");
    printf("=====================================\n\n");
    
    if(current == NULL) {
        printf("No tasks found. Add some tasks first!\n\n");
        waitForEnter();
        return;
    }
    
    while(current != NULL) {
        taskCount++;
        printf("ID: %d\n", current->id);
        printf("Description: %s\n", current->description);
        printf("Status: %s\n", current->completed ? "[COMPLETED]" : "[PENDING]");
        printf("-------------------------------------\n");
        
        if(current->completed) {
            completedCount++;
        } else {
            pendingCount++;
        }
        
        current = current->next;
    }
    
    printf("\nSummary:\n");
    printf("Total Tasks: %d\n", taskCount);
    printf("Completed: %d\n", completedCount);
    printf("Pending: %d\n", pendingCount);
    printf("\n");
    waitForEnter();
}

// Mark a task as complete
void markComplete() {
    int taskId;
    Task* current = head;
    int found = 0;
    
    if(head == NULL) {
        printf("\nNo tasks available to mark as complete!\n");
        waitForEnter();
        return;
    }
    
    viewTasks();
    printf("Enter the ID of task to mark as complete: ");
    taskId = getIntegerInput();
    
    while(current != NULL) {
        if(current->id == taskId) {
            if(current->completed) {
                printf("\nTask ID %d is already completed!\n", taskId);
            } else {
                current->completed = 1;
                printf("\nTask ID %d marked as complete!\n", taskId);
            }
            found = 1;
            break;
        }
        current = current->next;
    }
    
    if(!found) {
        printf("\nTask ID %d not found!\n", taskId);
    }
    
    waitForEnter();
}

// Delete a task
void deleteTask() {
    int taskId;
    Task* current = head;
    Task* previous = NULL;
    int found = 0;
    
    if(head == NULL) {
        printf("\nNo tasks available to delete!\n");
        waitForEnter();
        return;
    }
    
    viewTasks();
    printf("Enter the ID of task to delete: ");
    taskId = getIntegerInput();
    
    while(current != NULL) {
        if(current->id == taskId) {
            if(previous == NULL) {
                head = current->next;
            } else {
                previous->next = current->next;
            }
            free(current);
            printf("\nTask ID %d deleted successfully!\n", taskId);
            found = 1;
            break;
        }
        previous = current;
        current = current->next;
    }
    
    if(!found) {
        printf("\nTask ID %d not found!\n", taskId);
    }
    
    waitForEnter();
}

// Save tasks to file
void saveToFile() {
    FILE* file = fopen(FILENAME, "w");
    Task* current = head;
    
    if(file == NULL) {
        printf("Error: Could not save to file!\n");
        return;
    }
    
    // Write task count for loading
    int count = 0;
    current = head;
    while(current != NULL) {
        count++;
        current = current->next;
    }
    fprintf(file, "%d\n", count);
    
    // Write all tasks
    current = head;
    while(current != NULL) {
        fprintf(file, "%d\n", current->id);
        fprintf(file, "%s\n", current->description);
        fprintf(file, "%d\n", current->completed);
        current = current->next;
    }
    
    // Update taskIdCounter
    if(count > 0) {
        current = head;
        int maxId = 0;
        while(current != NULL) {
            if(current->id > maxId) {
                maxId = current->id;
            }
            current = current->next;
        }
        taskIdCounter = maxId + 1;
    }
    
    fprintf(file, "%d\n", taskIdCounter);
    
    fclose(file);
}

// Load tasks from file
void loadFromFile() {
    FILE* file = fopen(FILENAME, "r");
    Task* current;
    int count, i;
    int id, completed;
    char description[MAX_TASK_LENGTH];
    
    if(file == NULL) {
        // File doesn't exist, start fresh
        return;
    }
    
    // Free existing tasks
    freeTasks();
    head = NULL;
    
    // Read task count
    if(fscanf(file, "%d\n", &count) != 1) {
        fclose(file);
        return;
    }
    
    // Read tasks
    for(i = 0; i < count; i++) {
        if(fscanf(file, "%d\n", &id) != 1) break;
        fgets(description, MAX_TASK_LENGTH, file);
        description[strcspn(description, "\n")] = 0;
        if(fscanf(file, "%d\n", &completed) != 1) break;
        
        Task* newTask = (Task*)malloc(sizeof(Task));
        if(newTask == NULL) {
            printf("Memory allocation failed while loading!\n");
            fclose(file);
            return;
        }
        
        newTask->id = id;
        strcpy(newTask->description, description);
        newTask->completed = completed;
        newTask->next = NULL;
        
        if(head == NULL) {
            head = newTask;
        } else {
            current = head;
            while(current->next != NULL) {
                current = current->next;
            }
            current->next = newTask;
        }
    }
    
    // Read taskIdCounter if available
    if(fscanf(file, "%d\n", &taskIdCounter) != 1) {
        // If not found, calculate from loaded tasks
        if(head != NULL) {
            current = head;
            int maxId = 0;
            while(current != NULL) {
                if(current->id > maxId) {
                    maxId = current->id;
                }
                current = current->next;
            }
            taskIdCounter = maxId + 1;
        } else {
            taskIdCounter = 1;
        }
    }
    
    fclose(file);
}

// Free all tasks from memory
void freeTasks() {
    Task* current = head;
    Task* next;
    
    while(current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
    
    head = NULL;
}

// Clear screen (cross-platform)
void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

// Wait for user to press Enter
void waitForEnter() {
    printf("\nPress Enter to continue...");
    fflush(stdin);
    getchar();
}

// Get integer input safely
int getIntegerInput() {
    int num;
    char buffer[100];
    
    if(fgets(buffer, sizeof(buffer), stdin) != NULL) {
        if(sscanf(buffer, "%d", &num) == 1) {
            return num;
        }
    }
    return -1; // Invalid input
}
