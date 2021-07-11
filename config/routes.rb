Rails.application.routes.draw do
  devise_for :users, controllers: {
    sessions: 'users/sessions'
  }
  # For details on the DSL available within this file, see https://guides.rubyonrails.org/routing.html
  root 'tops#index'

  # 個体の情報関連
  get 'kerberos/signup', to: 'kerberos#new'
  post 'kerberos', to: 'kerberos#create'
  get 'kerberos/login', to: 'kerberos#login'
  post 'kerberos/login', to: 'kerberos#login'
  post 'kerberos/logout',to: 'kerberos#logout'
  get 'kerberos', to: 'kerberos#index'
  get 'kerberos/edit', to: 'kerberos#edit'
  post 'kerberos/update', to: 'kerberos#update'

  # ソフトの本質部分
  # 睡眠シフト
  get 'kerberos/sleep', to: 'sleeps#index'
  get 'kerberos/sleep/show', to: 'sleeps#show'
  get 'kerberos/sleep/edit', to: 'sleeps#edit'
  post 'kerberos/sleep/create', to: 'sleeps#create'
  post 'kerberos/sleep/confirm', to: 'sleeps#confirm'
  # エサログ
  get 'kerberos/eatlog', to: 'eats#index'
  get 'kerberos/eatlog/new', to: 'eats#new'
  get 'kerberos/eatlog/create', to: 'eats#create'
  # マッチング
  get 'kerberos/matching', to: 'matchings#index'
  get 'kerberos/matching/following', to: 'matchings#following'
  get 'kerberos/matching/follower',to: 'matchings#follower'
  post 'kerberos/matching/follow', to: 'matchings#follow'

  # 頭の情報関連
  get "head", to: "heads#index"
  get "head/setting", to: 'users#set_id'
end
