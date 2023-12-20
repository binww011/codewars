def find_outlier(integers):
  even = [i for i in integers if not i%2]
  oddn = [i for i in integers if i%2]
  return even[0] if len(even) < len(oddn) else oddn[0]
