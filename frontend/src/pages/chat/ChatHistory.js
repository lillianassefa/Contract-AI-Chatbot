import { List, Box, Typography } from '@mui/material'

const SingleChat = (props) => {
  return (
    <Box
      sx={{
        margin: props.isUser ? '20px 0px 0px 80px' : '20px 60px 0px 0px',
        marginBottom: '10px',
        padding: '10px',
        background: props.isUser ? '#AAAAAA' : '#C2B9EF',
        borderRadius: props.isUser ? '10px 0px 0px 10px' : '0px 10px 10px 0px',
      }}
    >
      <Typography variant="body1">
        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Itaque veniam
        amet officiis doloribus ad nihil dignissimos. Consequatur,
        necessitatibus totam dolorem autem quia sit temporibus cumque similique
        vitae numquam error maxime.
      </Typography>
    </Box>
  )
}

const ChatHistory = () => {
  return (
    <List sx={{ overflowY: 'auto' }}>
      <SingleChat />
      <SingleChat isUser="true" />
      <SingleChat />
      <SingleChat isUser="true" />
      <SingleChat />
      <SingleChat isUser="true" />
      <SingleChat />
      <SingleChat isUser="true" />
    </List>
  )
}
export default ChatHistory
