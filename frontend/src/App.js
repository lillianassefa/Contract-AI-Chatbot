// // App.js
import { Stack } from "@mui/material";
import Topbar from "./pages/TopBar/TopBar";
import Chat from "./pages/chat/chat";

function App() {

  return (
    <Stack spacing={2}>
      <Topbar />
      <Stack
        direction={"row"}
        spacing={2}
        sx={{ padding: "0px 30px" }}
        justifyContent={"right"}
      >
        <Chat />
      </Stack>
    </Stack>
  );
}

export default App;
