import { IconButton, Stack, TextField, Typography } from '@mui/material'
import SendIcon from '@mui/icons-material/Send'
import DeleteIcon from '@mui/icons-material/Delete'
import AttachFileIcon from '@mui/icons-material/AttachFile'
import { styled } from '@mui/material/styles'
import { useState, useRef } from 'react'

const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
})

const ChatInput = () => {
  const userInputRef = useRef(null)

  const [file, setFile] = useState(null)

  const handleChange = (event) => {
    setFile(event.target.files[0])
    console.log('filename', event.target.files[0])
  }

  const onSend = () => {
    console.log('userInput', userInputRef.current.value)
    userInputRef.current.value = ''
  }
  return (
    <Stack sx={{ padding: '0px 0px 20px 15px' }}>
      <Stack direction={'row'}>
        <TextField
          inputRef={userInputRef}
          variant="standard"
          placeholder="Paste your text here..."
          sx={{
            width: '100%',
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
        <Stack direction={'row'} spacing={2} alignItems={'center'}>
          <Typography sx={{ fontSize: '12px' }}>{file['name']}</Typography>
          <IconButton onClick={() => setFile(null)} size="small">
            <DeleteIcon />
          </IconButton>
        </Stack>
      )}
    </Stack>
  )
}
export default ChatInput
