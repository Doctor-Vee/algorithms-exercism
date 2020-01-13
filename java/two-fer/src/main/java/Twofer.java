class Twofer {
    String twofer(String name) {
        try{
            String output = (!name.isEmpty()) ? name : "you";
            return "One for " + output + ", one for me.";
            } catch (NullPointerException e){
                return "One for you, one for me.";
            }
    }
}
