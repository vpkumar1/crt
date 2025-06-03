public class largestnumberfinder
{
public static void main(String[]args)
{
int[] numbers{34,78,12,56,89,23};
int max=numbers[0];
for(int num:numbers)
{
if(num>max)
{max=num;}
}
System.out.println("the largest number is:"+max);
}
}