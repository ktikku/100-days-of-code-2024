# Time Complexity: O(n)
# Space Complexity: O(1)

#Approach: We simulate the cooking process by iterating over the customers and calculating the waiting time for each customer.
#We maintain the current time and the waiting time for each customer.
#If the customer arrives after the current time, we update the current time to the arrival time of the customer and add the cooking time to the waiting time.
#If the customer arrives before the current time, we add the waiting time to the current time and update the waiting time.
#Finally, we return the average waiting time by dividing the total waiting time by the number of customers.

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 0
        waiting_time = 0
        for customer in customers:
            arrival_time = customer[0]
            cooking_time = customer[1]
            if arrival_time >= current_time:
                current_time = arrival_time
                waiting_time = waiting_time + cooking_time
                current_time = current_time + cooking_time
            else:
                waiting_time = waiting_time + current_time + cooking_time - arrival_time
                current_time = current_time + cooking_time
        return waiting_time/len(customers)



        