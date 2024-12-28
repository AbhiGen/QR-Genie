// Import required modules
import inquirer from 'inquirer';
import qr from 'qr-image';
import fs from 'fs';

// Prompt user for input using inquirer
inquirer
  .prompt([
    {
      type: 'input',
      name: 'url',
      message: 'Enter a URL to generate its QR code:',
    },
  ])
  .then((answers) => {
    const userInput = answers.url;

    // Generate QR code from user input
    const qrFileName = 'qrcode.png';
    const qrCode = qr.image(userInput, { type: 'png' });

    // Save the QR code as an image file
    qrCode.pipe(fs.createWriteStream(qrFileName));
    console.log(`QR code has been saved as ${qrFileName}.`);

    // Save user input to a text file
    const textFileName = 'user_input.txt';
    fs.writeFile(textFileName, userInput, (err) => {
      if (err) {
        console.error('Error saving user input:', err);
      } else {
        console.log(`User input has been saved in ${textFileName}.`);
      }
    });
  })
  .catch((error) => {
    console.error('An error occurred:', error);
  });
