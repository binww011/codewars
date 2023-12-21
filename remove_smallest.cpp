#include <vector>

std::vector<unsigned int> removeSmallest(const std::vector<unsigned int>& numbers) {
  std::vector<unsigned int> numbers_r = {};
  int smallest = numbers[0], l_index, n_rep = 0;
  
  for (int e : numbers) {
    if (e < smallest)
      smallest = e;
  }
  
  for (int i : numbers)
    if (i == smallest) ++n_rep;
  
  if (n_rep > 0) {
    for (unsigned long long k = 0; k < numbers.size(); ++k)
      if (numbers[k] == smallest) {
        l_index = k;
        break;
      }
    for (unsigned long long i = 0; i < numbers.size(); ++i)
      if (numbers[i] != smallest || i != l_index) numbers_r.push_back(numbers[i]);
  } else {
    for (int t : numbers) {
      if (t != smallest)
        numbers_r.push_back(t);
    }
  }
  return numbers_r;
}
