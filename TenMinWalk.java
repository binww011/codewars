public class TenMinWalk {
  public static boolean isValid(char[] walk) {
    int k = 0, z = 0, n = 0;
    
    for (int i = 0; i < walk.length; ++i) {
      if (walk[i] == 's') {
        z += 1;
      } else if (walk[i] == 'n') {
        z -= 1;
      } else if (walk[i] == 'e') {
        k += 1;
      } else {
        k -= 1;
      }
      n += 1;
    }
    
    if (k == 0 && z == 0 && n == 10) {return true;}
    else return false;
  }
}
