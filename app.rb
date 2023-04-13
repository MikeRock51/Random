require 'sinatra'

get '/' do
    "Hello World"
end

post '/' do
    "We dey post"
end

post '/:password' do
    if params()
end