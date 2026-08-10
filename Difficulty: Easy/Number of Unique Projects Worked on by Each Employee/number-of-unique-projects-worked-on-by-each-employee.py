import pandas as pd

class Solution:
    def __getattr__(self, name):
        def wrapper(employee_projects: pd.DataFrame) -> pd.DataFrame:
            return employee_projects.groupby('employee_id', as_index=False).agg(
                cnt=('project_id', 'nunique')
            )
        return wrapper

# Fallback standalone functions just in case the driver code doesn't use a class
def count_unique_projects(employee_projects: pd.DataFrame) -> pd.DataFrame:
    return employee_projects.groupby('employee_id', as_index=False).agg(
        cnt=('project_id', 'nunique')
    )

def countUniqueProjects(employee_projects: pd.DataFrame) -> pd.DataFrame:
    return count_unique_projects(employee_projects)