import 'package:flutter/material.dart';
import 'app_pallete.dart';

class Apptheme {
  static final darkThemeMode = ThemeData.dark().copyWith(
    scaffoldBackgroundColor: Pallete.backgroundColor,
    inputDecorationTheme: InputDecorationTheme(
      enabledBorder: OutlineInputBorder(
        borderSide: const BorderSide(color: Pallete.borderColor),
        borderRadius: BorderRadius.circular(10),
      ),
      focusedBorder: OutlineInputBorder(
        borderSide: const BorderSide(color: Pallete.gradient1),
        borderRadius: BorderRadius.circular(10),
      ),
    )
  );
}
