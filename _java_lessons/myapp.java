///////////////////////////
/// 第３回 初めてのjava ///
///////////////////////////
// Q. printlnで"Hello World"と表示してみよう

// public class myapp{
//   public static void main(String[] args){
//     System.out.println("Hello World");
//   }
// }

/////////////////////////////////
/// 第４回 変数を使ってみよう ///
/////////////////////////////////

// public class myapp{
//   public static void main(String[] args){
//     String msg;
//     msg = "Hello World again";
// 
//     System.out.println(msg);
//   }
// }

///////////////////////////
/// 第８回 ifで条件分岐 ///
///////////////////////////
// public class myapp {
// 
//   public static void main(String[] args) {
//     // if
//     // > >= < <= == !=
//     // && || !
//     int score = 95;
//     if (score > 80) {
//       System.out.println("Great!");
//     } else if (score > 60) {
//       System.out.println("Good!");
//     } else {
//       System.out.println("so so ... !");
//     }
//   }
// }


///////////////////////////////
/// 第９回 switchで条件分岐 ///
///////////////////////////////
// public class myapp {
// 
//   public static void main(String[] args) {
//     // if
//     // > >= < <= == !=
//     // && || !
//     String signal = "red";
//     switch (signal) {
//       case "red":
//         System.out.println("stop!");
//         break;
//       case "blue":
//         System.out.println("go");
//         break;
//       case "yellow":
//         System.out.println("caution");
//         break;
//       default:
//         System.out.println("wrong signal");
//         break;
//     }
//   }
// }



////////////////////////////////
/// 第11回 forで繰り返し処理 ///
////////////////////////////////
// public class myapp {
// 
//   public static void main(String[] args) {
//     for(int i = 0; i < 10; i++){
//       if(i == 5){
//         break;
//       }
//       System.out.println(i);
//     }
//   }
// }



/////////////////////////////////
/// 第12回 配列を使って見よう ///
/////////////////////////////////
// public class myapp {
// 
//   public static void main(String[] args) {
//     // sales1, sales2, ...
//     // sales
// 
//      // int[] sales;
//      // sales = new int[3];
//      // sales[0] = 100;
//      // sales[1] = 200;
//      // sales[2] = 300;
// 
//      // int[] sales;
//      // sales = new int[] {100, 200, 300};
// 
//      int[] sales = {100, 200, 300};
// 
// 
//      System.out.println(sales[1]); // 200
//      sales[1] = 1000;
//      System.out.println(sales[1]); // 
//   }
// }



///////////////////////////////
/// 第13回 配列を要素を操作 ///
///////////////////////////////

// public class myapp {
// 
//   public static void main(String[] args) {
//     // 配列
//     // sales.length
//     int[] sales = {700, 400, 500};
// 
//     // for (int i = 0; i < 3; i++) {
//     // for (int i = 0; i < sales.length; i++) {
//     //   System.out.println(sales[i]);
//     // }
// 
//     for (int sale : sales) {
//       System.out.println(sale);
//     }
//   }
// }



/////////////////////////////////////
/// 第16回 メソッドを使ってみよう ///
/////////////////////////////////////
// public class myapp {
// 
//   // method
// 
//   // public static void sayHi() {
//   // public static void sayHi(String name) {
//   public static String sayHi(String name) {
//     // System.out.println("Hi!");
//     // System.out.println("Hi! " + name);
//     return "Hi! " + name;
//   }
// 
//   public static void main(String[] args) {
//     // sayHi();
//     // sayHi("Tom");
//     // sayHi("Bob");
//     String msg = sayHi("Steve");
//     System.out.println(msg);
//   }
// 
// }

///////////////////////////////////////
/// 第17回 メソッドをオーバーロード ///
///////////////////////////////////////
// public class myapp {
// 
//   public static void sayHi(String name) {
//     // int x = 10;
//     System.out.println("Hi! " + name);
//   }
// 
//   // overload
// 
//   public static void sayHi() {
//     System.out.println("Hi! Nobody!");
//   }
// 
//   public static void main(String[] args) {
//     sayHi();
//     sayHi("Steve"); // 引数
//     // System.out.println(name);
//     // System.out.println(x);
//   }
// 
// }




///////////////////////////////////////////
/// 第19回 コンストラクタを使ってみよう ///
///////////////////////////////////////////

// class User {
//   String name;
// 
//   // constructor
//   User(String name) {
//     this.name = name;
//   }
// 
//   // this()
// 
//   User() {
//     // this.name = "Me!";
//     this("Me!");
//   }
// 
//   void sayHi() {
//     System.out.println("hi! " + this.name);
//   }
// }
// 
// public class myapp {
// 
//   public static void main(String[] args) {
//     User tom;
//     // tom = new User("Tom");
//     tom = new User();
//     System.out.println(tom.name);
//     tom.sayHi();
//   }
// 
// }




/////////////////////////////////////
/// 第20回 クラスを継承してみよう ///
/////////////////////////////////////

// class User {
//   String name;
// 
//   User(String name) {
//     this.name = name;
//   }
// 
//   void sayHi() {
//     System.out.println("hi! " + this.name);
//   }
// }
// 
// class AdminUser extends User {
// 
//   AdminUser(String name) {
//     super(name);
//   }
// 
//   void sayHello() {
//     System.out.println("hello! " + this.name);
//   }
// 
//   // override
//   @Override
//   void sayHi() {
//     System.out.println("[admin] hi! " + this.name);
//   }
// }
// 
// public class myapp {
// 
//   public static void main(String[] args) {
//     User tom = new User("tom");
//     System.out.println(tom.name);
//     tom.sayHi();
// 
//     AdminUser bob = new AdminUser("bob");
//     System.out.println(bob.name);
//     bob.sayHi();
//     bob.sayHello();
//   }
// 
// }
























