public class PangramChecker {
  public boolean check(String sentence) {
    char init = 'a';
    
    while (init < 'z') {
      if (!sentence.toLowerCase().contains(String.valueOf(init))) return false;
      else ++init;
    }
    
    return true;
  }
}
