import 'package:flutter/material.dart';
import 'feature/auth/view/pages/signup_page.dart';
import 'core/theme/theme.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme:Apptheme.darkThemeMode,
      debugShowCheckedModeBanner: false,
      home: const SignupPage(),
    );
  }
}

