import { Avatar, Stack, Typography } from '@mui/material'

const Topbar = () => {
  return (
    <Stack
      direction={'row'}
      spacing={4}
      alignItems={'center'}
      justifyItems={'center'}
      sx={{
        padding: '10px',
      }}
    >
      <Avatar src="/images/logo.jpg" sx={{ width: 56, height: 56 }} />

      <Typography variant="h1" sx={{ textAlign: 'center', fontSize: '26px' }}>
        LIZZY AI Contract Q&A RAG System
      </Typography>
    </Stack>
  )
}
export default Topbar
