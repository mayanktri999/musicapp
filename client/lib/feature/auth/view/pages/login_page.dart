import 'package:flutter/material.dart';
import 'package:musicapp/feature/auth/view/widgets/custom_field.dart';
import 'package:musicapp/feature/auth/view/widgets/auth_gradient_button.dart';
import 'package:musicapp/core/theme/app_pallete.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({ Key? key }) : super(key: key);

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final emailController = TextEditingController();
  final passwordController = TextEditingController();
  final _formKey = GlobalKey<FormState>();

  @override
  void dispose() {
    emailController.dispose();
    passwordController.dispose();
    super.dispose();
    _formKey.currentState?.validate();
  }
  Widget build(BuildContext context) {
    return Scaffold(
      appBar :AppBar(),
        body: Padding(
          padding: const EdgeInsets.all(15.0),
          child: Form(
            key: _formKey,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text('SignIn ',style: TextStyle(fontSize: 50),),
                const SizedBox(height: 30,),
                CustomField(hintText: "Gmail", controller: emailController,),
                const SizedBox(height: 20,),
                CustomField(hintText: "Password", controller: passwordController,
                obscureText: true,),
                const SizedBox(height: 20,),
                AuthGradientButton(buttonText: "SignIn", onTap: () {}),
                const SizedBox(height: 25,),
                RichText(text:  
                TextSpan(
                  text: "Don't have an account? ",
                  style:  TextStyle(color: Colors.white),
                  children: [
                    TextSpan(
                      text: "Signup",
                      style:  TextStyle(color: Pallete.gradient1, fontWeight: FontWeight.bold),
                      
                        // Handle login tap
                      
                    ),
                  ],
                ),
                ),
              ],
              
            ),
          ),
        ),
      
      
    );
  }
}