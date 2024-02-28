import { IconButton, Stack, TextField, Typography } from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import DeleteIcon from "@mui/icons-material/Delete";
import AttachFileIcon from "@mui/icons-material/AttachFile";
import { styled } from "@mui/material/styles";
import { useState, useRef } from "react";
import axios from "axios";

const VisuallyHiddenInput = styled("input")({
  clip: "rect(0 0 0 0)",
  clipPath: "inset(50%)",
  height: 1,
  overflow: "hidden",
  position: "absolute",
  bottom: 0,
  left: 0,
  whiteSpace: "nowrap",
  width: 1,
});

const ChatInput = (props) => {
  const userInputRef = useRef(null);

  const [file, setFile] = useState(null);

  const handleChange = (event) => {
    setFile(event.target.files[0]);
    console.log("filename", event.target.files[0]);
  };

  const onInteraction = (isUser, message, fileName) => {
    let interaction = {
      isUser: isUser,
      message: message,
      fileName: fileName,
    };

    props.setInteraction((prev) => {
      return [...prev, interaction];
    });
  };

  const onSend = async () => {
    let userInput = userInputRef.current.value;
    let filename = file != null ? file.name : null;

    onInteraction(true, userInput, filename);

    try {
      let formData = new FormData();

      formData.append("query", userInput);
      
      if (file) formData.append("file", file);
      

      const response = await axios.post(
        "http:///0.0.0.0:8004/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      console.log("b")


      let answer = response.data.Answer;
      console.log(answer)
      // props.setIsLoading(false)
      onInteraction(false, answer, null);

      userInputRef.current.value = "";
      setFile(null);
    } catch (error) {
      onInteraction(false, "Sorry, there seems to a problem");
    }
  };
  return (
    <Stack sx={{ padding: "0px 0px 20px 15px" }}>
      <Stack direction={"row"}>
        <TextField
          inputRef={userInputRef}
          variant="standard"
          placeholder="Paste your text here..."
          sx={{
            width: "100%",
          }}
        />
        <IconButton component="label">
          <AttachFileIcon />
          <VisuallyHiddenInput type="file" onChange={handleChange} />
        </IconButton>
        <IconButton onClick={onSend}>
          <SendIcon />
        </IconButton>
      </Stack>
      {file !== null && (
        <Stack direction={"row"} spacing={2} alignItems={"center"}>
          <Typography sx={{ fontSize: "12px" }}>{file["name"]}</Typography>
          <IconButton onClick={() => setFile(null)} size="small">
            <DeleteIcon />
          </IconButton>
        </Stack>
      )}
    </Stack>
  );
};
export default ChatInput;
