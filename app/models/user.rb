class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable, :trackable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable
         
  validates :position, inclusion: {in: %w(left center right)}
  validates :kerbero_id, presence: true

  def name
    @kerbero = Kerbero.find(self.kerbero_id)
    ret = @kerbero.name
    case self.position
    when "left"
      ret = "左" + ret
    when "center"
      ret = "中" + ret
    when "right"
      ret = "右" + ret
    end
  end
end
