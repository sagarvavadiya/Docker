const robot = require("robotjs");
const { app, BrowserWindow, screen } = require("electron");
// Get the current mouse cursor position
const mousePos = robot.getMousePos();
const activeWin = require("active-win");
const screenshot = require("node-screenshot");
// Find the screen that contains the mouse cursor
const screen2 = robot.getScreenSize();

const CurrentScreen2 = () => {
  const activeScreen = {
    id: 0,
    bounds: { x: 0, y: 0, width: screen2.width, height: screen2.height },
  };

  for (let i = 0; i < screen2.width; i++) {
    for (let j = 0; j < screen2.height; j++) {
      if (
        robot.getPixelColor(mousePos.x, mousePos.y) !==
        robot.getPixelColor(i, j)
      ) {
        // The pixel color under the cursor is different from the pixel color on this screen
        break;
      }
      activeScreen.id++;
      activeScreen.bounds.x += screen2.width;
      if (activeScreen.bounds.x + screen2.width > mousePos.x) {
        activeScreen.bounds.width = screen2.width;
        activeScreen.bounds.height = screen2.height;
        break;
      }
    }
    if (activeScreen.bounds.width !== screen2.width) {
      break;
    }
  }

  // Print information about the active screen
  console.log("Active Screen Details:", activeScreen);
  //   console.log(`ID: ${activeScreen.id}`);
  //   console.log(`Bounds: ${JSON.stringify(activeScreen.bounds)}`);
  return "ok";
};

const CurrentScreen = () => {
  // Get the screen that currently has the keyboard and mouse focus
  app.on("ready", () => {
    const mainWindow = new BrowserWindow({ width: 800, height: 600 });

    // Get the screen that currently has the keyboard and mouse focus
    const activeScreen = screen.getDisplayNearestPoint(
      screen.getCursorScreenPoint()
    );

    // Print information about the active screen
    console.log("Active Screen Details:");
    console.log(`ID: ${activeScreen.id}`);
    console.log(`Bounds: ${JSON.stringify(activeScreen.bounds)}`);
    console.log(`Work Area: ${JSON.stringify(activeScreen.workArea)}`);

    // Load your application's HTML file or perform other actions.
    mainWindow.loadFile("index.html");
  });

  return "ok";
};

const TakeActiveScreen = () => {
  // activeWin().then(result => {
  //   if (result) {
  //     const activeWindowId = result.id;

  //     // Capture a screenshot of the active window
  //     screenshot({
  //       screen: {
  //         windowId: activeWindowId,
  //       },
  //       filename: 'active_window_screenshot.png', // Change this to your desired filename
  //     }, (err, imagePath) => {
  //       if (err) {
  //         console.error('Error capturing screenshot:', err);
  //       } else {
  //         console.log('Screenshot captured:', imagePath);
  //       }
  //     });
  //   } else {
  //     console.error('No active window found.');
  //   }
  // });
  console.log("process", process);
  return process.platform;
};
module.exports = { CurrentScreen, CurrentScreen2, TakeActiveScreen };
