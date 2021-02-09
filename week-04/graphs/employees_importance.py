class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        tot_importance = [0]
        self.importance_getter(employees, id, tot_importance)
        return tot_importance[0]
    def importance_getter(self, employees, id, tot_importance):
        for employee in employees:
            if employee.id == id:
                tot_importance[0] +=  employee.importance
                if not employee.subordinates:
                    return
                for subordinate in employee.subordinates:
                    self.importance_getter(employees, subordinate, tot_importance)