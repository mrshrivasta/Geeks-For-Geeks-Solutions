import pandas as pd
import numpy as np

class Solution:
    # A catch-all method in case the driver code uses an unknown method name
    def __getattr__(self, name):
        def wrapper(products: pd.DataFrame) -> pd.DataFrame:
            # Check if product_id is even and category starts with 'A'
            condition = (products['product_id'] % 2 == 0) & (products['category'].str.startswith('A', na=False))
            
            # Calculate discount
            discount_values = np.where(condition, products['price'], 0)
            
            # Create the result DataFrame
            result = pd.DataFrame({
                'product_id': products['product_id'],
                'discount': discount_values
            })
            
            # Return ordered by product_id in ascending order
            return result.sort_values(by='product_id').reset_index(drop=True)
        return wrapper