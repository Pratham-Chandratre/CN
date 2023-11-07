
import java.net.*;
import java.util.*;
public class IPDemo
{
 public static void main(String[] args){
 String host;
 Scanner ch = new Scanner(System.in); 
 System.out.print("1.Enter Host Name \n2.Enter IP address \nChoice=");
 int choice = ch.nextInt();
 if(choice==1)
 { 
 Scanner input = new Scanner(System.in);
 System.out.print("\n Enter host name: ");
 host = input.nextLine();
 try {
 InetAddress address = InetAddress.getByName(host);
 System.out.println("IP address: " + address.getHostAddress());
 System.out.println("Host name : " + address.getHostName()); 
 System.out.println("Host name and IP address: " + address.toString());
 }
 catch (UnknownHostException ex) {
 System.out.println("Could not find " + host);
 }
 }
 else
 {
 Scanner input = new Scanner(System.in);
 System.out.print("\n Enter IP address: ");
 host = input.nextLine();
 try {
 InetAddress address = InetAddress.getByName(host);
 System.out.println("Host name : " + address.getHostName()); 
 System.out.println("IP address: " + address.getHostAddress());
 System.out.println("Host name and IP address: " + address.toString());
 }
 catch (UnknownHostException ex) {
 System.out.println("Could not find " + host);
 }
 }
 
 }
}
/*OUTPUT
iotlab@iotlab-Veriton-M200-B360:~$ javac IPDemo.java 
iotlab@iotlab-Veriton-M200-B360:~$ java IPDemo 
1.Enter Host Name 
2.Enter IP address 
Choice=1
 Enter host name: www.google.com
IP address: 172.217.160.196
Host name : www.google.com
Host name and IP address: www.google.com/172.217.160.196
iotlab@iotlab-Veriton-M200-B360:~$ java IPDemo 
1.Enter Host Name 
2.Enter IP address 
Choice=2
 Enter IP address: 8.8.8.8
Host name : dns.google
IP address: 8.8.8.8
Host name and IP address: dns.google/8.8.8.8
iotlab@iotlab-Veriton-M200-B360:~$ 
*/