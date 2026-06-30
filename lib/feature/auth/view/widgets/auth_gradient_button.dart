import 'package:flutter/material.dart';
import 'package:musicapp/core/theme/app_pallete.dart';

class AuthGradientButton extends StatelessWidget {
  const AuthGradientButton({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors:[ Pallete.gradient1, Pallete.gradient2],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(10),
      ),
      child: ElevatedButton(
        onPressed: () {},
        style: ElevatedButton.styleFrom(
          fixedSize:const Size(395, 55),
          backgroundColor:  Pallete.transparentColor,
          shadowColor: Pallete.transparentColor),
        child: const Text('Sign Up', style: TextStyle(fontSize: 17,fontWeight: FontWeight.w500, color: Colors.white),),
      ),
    );
  }
}