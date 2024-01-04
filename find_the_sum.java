public class Sum {
  public int GetSum(int a, int b) {
    int lt = (a < b) ? a : b;
    int gt = (a > b) ? a : b;
    int response = 0;
    for (int i = lt; i <= gt; ++i) response += i;
    return response;
  }
}
