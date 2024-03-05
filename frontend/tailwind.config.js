/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx,html}"],
  darkMode: "class", // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: {
          DEFAULT: "#0a71d0",
          dark: "rgb(7,79,145)",
          light: "rgb(59, 121, 217)",
        },
        secondary: "#309cff",
        error: "d7354a",
      },
    },
  },
  plugins: [],
};
