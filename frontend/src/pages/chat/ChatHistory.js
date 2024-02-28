import { List, Box, Typography, Stack} from '@mui/material'
import FilePresentIcon from '@mui/icons-material/FilePresent'

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
      {props.fileName != null && (
        <Stack direction={'row'} spacing={2}>
          <FilePresentIcon />
          <Typography variant="body1"> {props.fileName}</Typography>
        </Stack>
      )}
      {props.fileName != null && <Box height={'10Px'} />}
      {props.message != null && (
        <Typography variant="body1">{props.message}</Typography>
      )}
    </Box>
  )
}

const ChatHistory = (props) => {
  return (
    <List sx={{ overflowY: 'auto' }}>
      {props.interaction.map((e, index) => {
        return <SingleChat key={index} {...e} />
      })}
      {/* {props.isLoading && (
        <Box padding={'0px 15px'}>
          <CircularProgress size={'30px'} />
        </Box>
      )} */}
    </List>
  )
}
export default ChatHistory