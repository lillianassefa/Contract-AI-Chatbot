import { Box, Stack, Button, IconButton, Avatar } from '@mui/material'
import ChatInput from './ChatInput'
import ChatHistory from './ChatHistory'
import { useState } from 'react'
import ChatIcon from '@mui/icons-material/Chat'

const Chat = () => {
  const [isHidden, setHide] = useState(false)

  const [interaction, setInteraction] = useState([])

  const [isLoading, setIsLoading] = useState(false)

  return isHidden ? (
    <IconButton
      onClick={() => setHide(false)}
      sx={{ position: 'fixed', right: 40, bottom: 20 }}
    >
      <Avatar sx={{ height: 50, width: 50 }}>
        <ChatIcon />
      </Avatar>
    </IconButton>
  ) : (
    <Box
      sx={{
        position: 'fixed',
        right: 0,
        bottom: 0,
        width: '40%',
        height: 'calc(80vh - 50px)',
        background: '#f8f8f8',
      }}
    >
      <Button onClick={() => setHide(true)}>Hide</Button>
      <Stack justifyContent="space-between" spacing={2} sx={{ height: '95%' }}>
        <ChatHistory interaction={interaction} isLoading={isLoading} />
        <ChatInput
          setInteraction={setInteraction}
          setIsLoading={setIsLoading}
        />
      </Stack>
    </Box>
  )
}
export default Chat
